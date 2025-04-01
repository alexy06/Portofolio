import mongoose from "mongoose";

export const connectDB = async () => {
  await mongoose
    .connect(
      "mongodb+srv://alexizot99:oyvcV4cSXp9fnGpA@cluster0.srkrw.mongodb.net/food-del"
    )
    .then(() => {
      console.log("DB Connected");
    });
};
