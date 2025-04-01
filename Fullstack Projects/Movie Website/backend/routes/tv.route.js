import express from "express";
import {
  getDetailsTv,
  getSimilarTVs,
  getTrailersTv,
  getTrendingTv,
  getTVsByCategory,
} from "../controllers/tv.controller.js";

const router = express.Router();

router.get("/trending", getTrendingTv);
router.get("/:id/trailers", getTrailersTv);
router.get("/:id/details", getDetailsTv);
router.get("/:id/similar", getSimilarTVs);
router.get("/:category", getTVsByCategory);

export default router;
