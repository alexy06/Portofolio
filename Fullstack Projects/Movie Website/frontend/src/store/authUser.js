import axios from "axios";
import toast from "react-hot-toast";
import { create } from "zustand";

export const useAuthStore = create((set) => ({
  user: null,
  isSigninUp: false,
  isCheckingAuth: true,
  isLoggingOut: false,
  isLoggingIn: false,
  signup: async (credentials) => {
    set({ isSigninUp: true });
    try {
      const response = await axios.post("/api/v1/auth/signup", credentials);
      set({ user: response.data.user, isSigninUp: false });
      toast.success("Signup successful!");
    } catch (error) {
      toast.error(error.response.data.message || "Signup failed");
      set({ user: null, isSigninUp: false });
      console.log(error);
    }
  },
  login: async (credentials) => {
    set({ isLoggingIn: true });
    try {
      const response = await axios.post("/api/v1/auth/login", credentials);
      set({ user: response.data.user, isLoggingIn: false });
      console.log(response.data.user);
    } catch (error) {
      set({ isLoggingIn: false, user: null });
      toast.error(error.response.data.message || "Login failed");
    }
  },
  logout: async () => {
    set({ isLoggingOut: true });
    try {
      await axios.post("/api/v1/auth/logout");
      set({ user: null, isLoggingOut: false });
      toast.success("Logged out successfully!");
    } catch (error) {
      set({ isLoggingOut: false });
      toast.error(error.response.data.message || "Logout failed");
    }
  },
  authCheck: async () => {
    set({ isCheckingAuth: true });
    try {
      const response = await axios.get("/api/v1/auth/authCheck");
      set({ user: response.data.user, isCheckingAuth: false });
    } catch (error) {
      set({ isCheckingAuth: false, user: null });
      console.log(error);
    }
  },
}));
