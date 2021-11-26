let hello = (req, res) => {
    res.status(200).json({
        message: "hello world! this is Serverless workshop! BYE!!"
    });
}

export default hello;