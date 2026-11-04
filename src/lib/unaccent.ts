/**
 * Normalizes Vietnamese text by removing accents/diacritics for flexible search
 * Example: "Khai vấn chánh niệm" -> "khai van chanh niem"
 */
export function removeVietnameseAccents(str: string): string {
  if (!str) return "";
  return str
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[đĐ]/g, (m) => (m === "đ" ? "d" : "D"))
    .toLowerCase()
    .trim();
}

export function searchMatches(target: string, query: string): boolean {
  if (!query) return true;
  if (!target) return false;
  const normTarget = removeVietnameseAccents(target);
  const normQuery = removeVietnameseAccents(query);
  return normTarget.includes(normQuery);
}
