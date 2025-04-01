import express from "express";
import {
  getSearchHistory,
  removeItemFromSearchHistory,
  searchMovies,
  searchPerson,
  searchTv,
} from "../controllers/search.controller.js";

const router = express.Router();

router.get("/person/:query", searchPerson);
router.get("/movie/:query", searchMovies);
router.get("/tv/:query", searchTv);

router.get("/history", getSearchHistory);

router.delete("/history/:id", removeItemFromSearchHistory);

export default router;
