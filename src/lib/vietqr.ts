/**
 * Dynamic VietQR Generator & Bank Transfer Helper
 */

export interface VietQrParams {
  bankBin: string;
  accountNumber: string;
  accountHolder: string;
  amount: number;
  orderCode: string;
}

export function generateVietQrUrl(params: VietQrParams): string {
  const { bankBin, accountNumber, accountHolder, amount, orderCode } = params;
  const cleanAccount = accountNumber.replace(/\s+/g, "");
  const encodedHolder = encodeURIComponent(accountHolder);
  const encodedOrderCode = encodeURIComponent(orderCode);
  
  // VietQR Standard format
  // https://img.vietqr.io/image/<BANK_BIN>-<ACCOUNT_NUMBER>-compact2.png?amount=<AMOUNT>&addInfo=<ORDER_CODE>&accountName=<NAME>
  return `https://img.vietqr.io/image/${bankBin}-${cleanAccount}-compact2.png?amount=${amount}&addInfo=${encodedOrderCode}&accountName=${encodedHolder}`;
}

export function formatVnd(amount: number): string {
  return new Intl.NumberFormat("vi-VN", {
    style: "currency",
    currency: "VND",
  }).format(amount);
}
