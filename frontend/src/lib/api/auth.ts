import { apiClient, setAccessToken, setRefreshToken, clearTokens } from "./client";

export interface TokenPair {
  access_token: string;
  refresh_token: string;
  token_type: string;
}

export async function loginUser(email: string, password: string): Promise<void> {
  const form = new URLSearchParams();
  form.append("username", email); // OAuth2PasswordRequestForm expects `username`
  form.append("password", password);

  const { data } = await apiClient.post<TokenPair>("/auth/login", form, {
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
  });

  setAccessToken(data.access_token);
  setRefreshToken(data.refresh_token);
}

export async function registerUser(name: string, email: string, password: string): Promise<void> {
  // `role` intentionally omitted — backend defaults to UserRole.STUDENT
  const { data } = await apiClient.post<TokenPair>("/auth/register", {
    name,
    email,
    password,
  });

  setAccessToken(data.access_token);
  setRefreshToken(data.refresh_token);
}

export function logoutUser(): void {
  clearTokens();
  // Note: this only clears local cookies. To also revoke server-side,
  // call apiClient.post("/auth/logout", { refresh_token: getRefreshToken() })
  // before clearing — left as a deliberate follow-up, see explanation below.
}