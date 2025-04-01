import express from "express";
import router from "./auth.route.js";
import {
  getTrendingMovie,
  getTrailersMovie,
  getDetailsMovie,
  getSimilarMovies,
  getMoviesByCategory,
} from "../controllers/movie.controller.js";

const routes = express.Router();

router.get("/trending", getTrendingMovie);
router.get("/:id/trailers", getTrailersMovie);
router.get("/:id/details", getDetailsMovie);
router.get("/:id/similar", getSimilarMovies);
router.get("/:category", getMoviesByCategory);

export default router;
