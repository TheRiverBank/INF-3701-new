import json


data  = {
  '_id': "61daf0c600f0af793e477e7b",
  'matchId': "61daf0c600f0af998e470e6a",
  'players': [ 
    { 
      'id': "61daf0c600f0af793e455e71", 
      'name': "ItsFootball", 
      'level': "Advanced"  
    },
    { 
      'id': "61daf0c600f0af793e455e60" , 
      'name': "ItsSoccer" , 
      'level': "Beginner"  
    } 
  ],
  'startDate': "2021-01-01T:10:00:00",
  'gamesPlayed': [
    {
      'gameId': 1, 
      'score': { 'ItsFootball' : 1, 'ItsSoccer' : 0 } 
    }
  ],
  'deviceDetails' : {
    'name' : "Playstation",
    'version' : "PS5" 
  }
}

with open("data.json", 'w') as f:
    f.write(json.dumps(data))
    