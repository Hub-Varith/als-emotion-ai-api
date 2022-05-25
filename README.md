# asl-emotion-ai-api

This api is designed for binary emotion classification using WordNetLemmatizer.
<h1>How to use the API:</h1>

### POST https://asl-emotion-ai-api.herokuapp.com/predict
#### Header:
```json
{"content-type":"application.json"}
```
#### Body:
```json
{"textdata":"text you want to predict"}
```
#### Response (returns "0" if negative, "1" if positive:

```json
{
  "data":"0"
}
```
