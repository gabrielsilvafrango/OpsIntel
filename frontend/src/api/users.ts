export interface UserCreate {
  name: string;
}

export interface User {
  id: number;
  name: string;
}

import { apiFetch } from "./client";

export function createUser(data: UserCreate) {
  return apiFetch<User>("/users/", {
    method: "POST",
    body: JSON.stringify(data),
  });
}
