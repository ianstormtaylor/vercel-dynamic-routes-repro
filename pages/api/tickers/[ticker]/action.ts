export default function(req, res) {
  return res.status(200).json(`Success: ${req.query.ticker}`)
}