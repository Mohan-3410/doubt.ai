from mongoengine import connect
import os

def db():
    connect(
        db='doubtmeai',
        host=f"mongodb+srv://{os.getenv('MONGOOSE_ID')}:{os.getenv('MONGOOSE_PASSWORD')}@cluster0.3r80h15.mongodb.net/doubtmeai?retryWrites=true&w=majority"
    )
    print("MongoDB connected")

