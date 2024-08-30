import mongoose from "mongoose";

export const connectDB = async () => {
    (await mongoose.connect('mongodb+srv://alexizot99:4382134163@cluster0.qvp72qo.mongodb.net/"Food Delivery"')).then(()=>console.log("DB Connected"));
}