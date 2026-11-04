-- ========================================================
-- SCHEMA: ICF PCC MENTOR (ZEN LÀNG MAI THEME)
-- Row Level Security (RLS) & Multi-Role Access Control (RBAC)
-- ========================================================

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "unaccent";

-- 1. PROFILES
CREATE TABLE IF NOT EXISTS public.profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    email TEXT NOT NULL UNIQUE,
    full_name TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'student' CHECK (role IN ('super_admin', 'editor', 'billing', 'student')),
    tier TEXT NOT NULL DEFAULT 'free' CHECK (tier IN ('free', '1_month', '6_months', '12_months')),
    tier_expires_at TIMESTAMPTZ,
    streak_count INT NOT NULL DEFAULT 0,
    last_active_date DATE,
    selected_sticker_pack TEXT DEFAULT 'monk_welcome',
    minimal_mode BOOLEAN DEFAULT FALSE,
    sound_enabled BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. SECTIONS (DYNAMIC MULTI-LEVEL TREE)
CREATE TABLE IF NOT EXISTS public.sections (
    id TEXT PRIMARY KEY,
    parent_id TEXT REFERENCES public.sections(id) ON DELETE CASCADE,
    code TEXT NOT NULL,
    title_vi TEXT NOT NULL,
    title_en TEXT NOT NULL,
    description_vi TEXT,
    description_en TEXT,
    nature_icon TEXT NOT NULL DEFAULT 'seed' CHECK (nature_icon IN ('seed', 'sprout', 'bamboo', 'lotus', 'mountain')),
    order_index INT NOT NULL DEFAULT 0,
    is_free BOOLEAN NOT NULL DEFAULT FALSE,
    is_published BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. THEORIES
CREATE TABLE IF NOT EXISTS public.theories (
    id TEXT PRIMARY KEY,
    section_id TEXT NOT NULL REFERENCES public.sections(id) ON DELETE CASCADE,
    title_vi TEXT NOT NULL,
    title_en TEXT NOT NULL,
    content_vi TEXT NOT NULL,
    content_en TEXT NOT NULL,
    video_url TEXT,
    attachments JSONB DEFAULT '[]'::jsonb,
    is_free BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. KEYWORDS
CREATE TABLE IF NOT EXISTS public.keywords (
    id TEXT PRIMARY KEY,
    section_id TEXT NOT NULL REFERENCES public.sections(id) ON DELETE CASCADE,
    term_vi TEXT NOT NULL,
    term_en TEXT NOT NULL,
    definition_vi TEXT NOT NULL,
    definition_en TEXT NOT NULL,
    category TEXT NOT NULL DEFAULT 'overview' CHECK (category IN ('mnemonic', 'overview')),
    memory_cue_vi TEXT,
    memory_cue_en TEXT,
    audio_term_en_url TEXT,
    order_index INT NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. FLASHCARDS
CREATE TABLE IF NOT EXISTS public.flashcards (
    id TEXT PRIMARY KEY,
    section_id TEXT NOT NULL REFERENCES public.sections(id) ON DELETE CASCADE,
    front_vi TEXT NOT NULL,
    front_en TEXT NOT NULL,
    back_vi TEXT NOT NULL,
    back_en TEXT NOT NULL,
    hint_vi TEXT,
    hint_en TEXT,
    order_index INT NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 6. USER FLASHCARD PROGRESS (LEITNER BOX)
CREATE TABLE IF NOT EXISTS public.user_flashcard_progress (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    flashcard_id TEXT NOT NULL REFERENCES public.flashcards(id) ON DELETE CASCADE,
    status TEXT NOT NULL DEFAULT 'unknown' CHECK (status IN ('known', 'unsure', 'unknown')),
    is_favorite BOOLEAN DEFAULT FALSE,
    review_count INT DEFAULT 0,
    last_reviewed_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, flashcard_id)
);

-- 7. CASE STUDIES
CREATE TABLE IF NOT EXISTS public.case_studies (
    id TEXT PRIMARY KEY,
    section_id TEXT NOT NULL REFERENCES public.sections(id) ON DELETE CASCADE,
    title_vi TEXT NOT NULL,
    title_en TEXT NOT NULL,
    scenario_dialogue_vi TEXT NOT NULL,
    scenario_dialogue_en TEXT NOT NULL,
    analysis_questions_vi TEXT NOT NULL,
    analysis_questions_en TEXT NOT NULL,
    suggested_answers_vi TEXT NOT NULL,
    suggested_answers_en TEXT NOT NULL,
    competency_mapping TEXT,
    pcc_markers JSONB DEFAULT '[]'::jsonb,
    order_index INT NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 8. QUIZZES
CREATE TABLE IF NOT EXISTS public.quizzes (
    id TEXT PRIMARY KEY,
    section_id TEXT REFERENCES public.sections(id) ON DELETE CASCADE,
    type TEXT NOT NULL DEFAULT 'standard_mcq' CHECK (type IN ('standard_mcq', 'icf_sjt')),
    question_vi TEXT NOT NULL,
    question_en TEXT NOT NULL,
    options JSONB NOT NULL,
    correct_answer TEXT,
    best_answer TEXT,
    worst_answer TEXT,
    explanation_vi TEXT NOT NULL,
    explanation_en TEXT NOT NULL,
    primary_competency TEXT,
    key_clue_vi TEXT,
    key_clue_en TEXT,
    difficulty TEXT DEFAULT 'medium' CHECK (difficulty IN ('easy', 'medium', 'hard')),
    order_index INT NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 9. EXAM SESSIONS
CREATE TABLE IF NOT EXISTS public.exam_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    section_id TEXT REFERENCES public.sections(id) ON DELETE SET NULL,
    exam_type TEXT NOT NULL CHECK (exam_type IN ('section_mock', 'full_pcc_mock', 'quick_tea')),
    score NUMERIC(5,2) NOT NULL DEFAULT 0,
    total_questions INT NOT NULL,
    correct_best_count INT DEFAULT 0,
    correct_worst_count INT DEFAULT 0,
    answers JSONB NOT NULL,
    duration_seconds INT NOT NULL DEFAULT 0,
    completed_at TIMESTAMPTZ DEFAULT NOW()
);

-- 10. LOTUS GARDEN (GAMIFICATION)
CREATE TABLE IF NOT EXISTS public.lotus_garden (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL UNIQUE REFERENCES public.profiles(id) ON DELETE CASCADE,
    seeds_planted INT DEFAULT 0,
    sprouts_grown INT DEFAULT 0,
    lotuses_bloomed INT DEFAULT 0,
    butterflies_unlocked INT DEFAULT 0,
    dragonflies_unlocked INT DEFAULT 0,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 11. ORDERS
CREATE TABLE IF NOT EXISTS public.orders (
    id TEXT PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    order_code TEXT NOT NULL UNIQUE,
    tier_id TEXT NOT NULL,
    amount NUMERIC(12,2) NOT NULL,
    discount_code TEXT,
    discount_amount NUMERIC(12,2) DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'pending_payment' CHECK (status IN ('pending_payment', 'pending_approval', 'approved', 'rejected', 'expired')),
    receipt_url TEXT,
    approved_by UUID REFERENCES public.profiles(id) ON DELETE SET NULL,
    approved_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 12. SYSTEM SETTINGS
CREATE TABLE IF NOT EXISTS public.system_settings (
    key TEXT PRIMARY KEY,
    value JSONB NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 13. MINDFULNESS MESSAGES
CREATE TABLE IF NOT EXISTS public.mindfulness_messages (
    id TEXT PRIMARY KEY,
    text_vi TEXT NOT NULL,
    text_en TEXT NOT NULL,
    theme TEXT NOT NULL,
    author TEXT DEFAULT 'Zen Wisdom',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 14. STICKERS
CREATE TABLE IF NOT EXISTS public.stickers (
    id TEXT PRIMARY KEY,
    code TEXT NOT NULL UNIQUE,
    name_vi TEXT NOT NULL,
    name_en TEXT NOT NULL,
    category TEXT NOT NULL CHECK (category IN ('monk', 'lotus', 'cat', 'nature', 'badge')),
    trigger_event TEXT NOT NULL,
    svg_content TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 15. AUDIT LOGS
CREATE TABLE IF NOT EXISTS public.audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES public.profiles(id) ON DELETE SET NULL,
    action TEXT NOT NULL,
    details TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 16. USER NOTES
CREATE TABLE IF NOT EXISTS public.user_notes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    section_id TEXT NOT NULL REFERENCES public.sections(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, section_id)
);

-- ========================================================
-- ROW LEVEL SECURITY (RLS) POLICIES
-- ========================================================

ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.sections ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.theories ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.keywords ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.flashcards ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_flashcard_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.case_studies ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.quizzes ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.exam_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.lotus_garden ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.orders ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.system_settings ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.mindfulness_messages ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.stickers ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.audit_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_notes ENABLE ROW LEVEL SECURITY;

-- Helper function: Check if current user is Super Admin
CREATE OR REPLACE FUNCTION public.is_super_admin()
RETURNS BOOLEAN AS $$
BEGIN
    RETURN EXISTS (
        SELECT 1 FROM public.profiles
        WHERE id = auth.uid() AND role = 'super_admin'
    );
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Helper function: Check if current user is Admin or Editor
CREATE OR REPLACE FUNCTION public.is_editor_or_admin()
RETURNS BOOLEAN AS $$
BEGIN
    RETURN EXISTS (
        SELECT 1 FROM public.profiles
        WHERE id = auth.uid() AND role IN ('super_admin', 'editor')
    );
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Helper function: Check if current user is Billing or Admin
CREATE OR REPLACE FUNCTION public.is_billing_or_admin()
RETURNS BOOLEAN AS $$
BEGIN
    RETURN EXISTS (
        SELECT 1 FROM public.profiles
        WHERE id = auth.uid() AND role IN ('super_admin', 'billing')
    );
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- RLS: Sections
CREATE POLICY "Public read published sections" ON public.sections
FOR SELECT USING (is_published = true OR public.is_editor_or_admin());

CREATE POLICY "Editor full manage sections" ON public.sections
FOR ALL USING (public.is_editor_or_admin());

-- RLS: Orders
CREATE POLICY "Users read own orders" ON public.orders
FOR SELECT USING (user_id = auth.uid() OR public.is_billing_or_admin());

CREATE POLICY "Users insert own orders" ON public.orders
FOR INSERT WITH CHECK (user_id = auth.uid());

CREATE POLICY "Billing approve orders" ON public.orders
FOR UPDATE USING (public.is_billing_or_admin());

-- RLS: System Settings
CREATE POLICY "Public read system settings" ON public.system_settings
FOR SELECT USING (true);

CREATE POLICY "Super admin manage system settings" ON public.system_settings
FOR ALL USING (public.is_super_admin());

-- RLS: Lotus Garden & Progress
CREATE POLICY "Users manage own garden" ON public.lotus_garden
FOR ALL USING (user_id = auth.uid());

CREATE POLICY "Users manage own notes" ON public.user_notes
FOR ALL USING (user_id = auth.uid());

CREATE POLICY "Users manage own flashcard progress" ON public.user_flashcard_progress
FOR ALL USING (user_id = auth.uid());

CREATE POLICY "Users view and insert exam sessions" ON public.exam_sessions
FOR ALL USING (user_id = auth.uid() OR public.is_editor_or_admin());
