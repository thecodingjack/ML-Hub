# ML-Hub

    
## Setup
Get docker https://docs.docker.com/install/
```sh

git clone https://github.com/thecodingjack/ML-Hub.git
Get docker herehttps://docs.docker.com/install/
docker-compose up --build

```

## Usage

### Creating a model
```sh

From repo root directory

$ bash app/create_model -i 1 -n test1 -t tips
-i : id | string
-n : name | string
-t : type | string (currently only 1 type)

Alternatively, use postman to create a model by sending

POST localhost:4000/experiment
and add json to body e.g. {"id":"1", "name": "test1", "type": "tips"}

```
### Training a model (with datasets from Seaborn)
```sh

$ bash app/train -i 1
-i : id | string

or

POST localhost:4000/train
and add json to body e.g. {"id":"1"}

```

### Testing a model (with datasets from Seaborn)
```sh

$ bash app/test -i 1
-i : id | string

or

GET localhost:4000/test
and add json to body e.g. {"id":"1"}

```
### Predict with a model
```sh

$ bash app/predict -i 1 -s [0,1,3,1,0,0,0]
-i : id | string
-s : sample | array[string] (variables of the model)

sample = [gender,smoker,party-size,Friday,Saturday,Sunday,dinner]
output = tips in USD 

or

POST localhost:4000/predict
and add json to body e.g. {"id":"1","sample": [0,1,3,1,0,0,0]}

```
