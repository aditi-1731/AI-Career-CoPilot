import { apiClient } from "./client";

export type UserRole = "student" | "admin" | string; // widen if you confirm exact enum values

export interface UserResponse {
  id: string;
  name: string;
  email: string;
  role: UserRole;
  is_verified: boolean;
}

export async function getCurrentUser(): Promise<UserResponse> {
  const { data } = await apiClient.get<UserResponse>("/users/me");
  return data;
}