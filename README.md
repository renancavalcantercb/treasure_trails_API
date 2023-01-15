# Treasure Trails API

A simple API that returns treasure trails data for a given player nickname in RuneScape 3.

## Prerequisites

- Python 3.x
- Flask
- Flask-RESTX
- requests
- pandas
- glob

## Installing

1. Clone the repository

`git clone https://github.com/renancavalcantercb/treasure_trails_API.git`

2. Install the required packages

`pip install -r requirements.txt`

3. Run the application

`python app.py`

## Usage

`/treasure_trails/{nickname}`

| Parameter | Type | Description |
| --- | --- | --- |
| `username` | `string` | The username of the player you want to get the stats from. |

## Example

+ `/treasure_trails/cutguardlan`
  + `200 OK`
  ```json
    [
      {
        "tier": "Easy",
        "quantity": "7125",
        "rank": "47"
      },
      {
        "tier": "Medium",
        "quantity": "10",
        "rank": "62912"
      },
      {
        "tier": "Hard",
        "quantity": "5016",
        "rank": "1103"
      },
      {
        "tier": "Elite",
        "quantity": "512",
        "rank": "8614"
      },
      {
        "tier": "Master",
        "quantity": "808",
        "rank": "1300"
      }
    ]
  ```
  
## Handling errors

If the API cannot find a player with the given nickname, it will return a 404 error with the message `Player {nickname} not found.`

```
{
  "error": "Player cutguardlan not found"
}
```

## Built With

- Flask - The web framework used
- Flask-RESTX - The toolkit used to build the API
- requests - Used to make requests to the Runescape API
- pandas - Used to manipulate and analyze the data
- glob - Used to find the CSV files
