import mongoose from 'mongoose'

const Schema = mongoose.Schema({
    proto: String,
    data: Array
})

export default mongoose.model('protos', Schema)