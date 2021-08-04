import express from 'express';
import mongoose from 'mongoose';
import dotenv from 'dotenv'
import cors from 'cors'
import Schemas from './Schema.js'

// AppConfig
const app = express();
const port = process.env.PORT || 9000;
dotenv.config()

// middlewares
app.use(express.json())
app.use(cors())

// DB config
const conn = process.env.CONN_URL;

//ROUTES
// app.get('/', (req, res) => {
//     res.send('We are live')
// })

//Connect tot DB
mongoose.connect(conn,
{
    useNewUrlParser: true,
    useCreateIndex: true,
    useUnifiedTopology: true
},
 () =>{
    console.log('Connected to facets DB!')
})

app.post('/', (req, res)=> {

    Schemas.create(req.body, (err,data) => {
        if (err) {
            res.status(500).send(err)
        } else {
            res.status(201).send(data)
        }
    })
});

app.post('/string', (req, res)=> {

    Schemas.create(req.body, (err,data) => {
        if (err) {
            res.status(500).send(err)
        } else {
            res.status(201).send(data)
        }
    })
});

app.get('/', (req, res)=> {

    Schemas.find((err,data) => {
        if (err) {
            res.status(500).send(err)
        } else {
            res.status(200).send(data)
        }
    })
});

app.get('/string', (req, res)=> {

    Schemas.find((err,data) => {
        if (err) {
            res.status(500).send(err)
        } else {
            res.status(200).send(data)
        }
    })
});

app.listen(port, ()=> console.log(`listening on localhost: ${port}`))
