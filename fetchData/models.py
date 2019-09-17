# importing flask libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import quandl

server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgres://pzqwpkpxcfsdqw:f88774a62ff43b0161debb7368ff54982fb2d4cf779256881116ecac045fe4f7@ec2-23-21-160-38.compute-1.amazonaws.com:5432/d5a5d8138qll8o'
db = SQLAlchemy(server)


class Stock(db.Model):
    __tablename__ = 'HD'
    Date = db.Column(db.Date, nullable=False, primary_key=True)
    Open = db.Column(db.Integer, nullable=False)
    High = db.Column(db.Integer, nullable=False)
    Low = db.Column(db.Integer, nullable=False)
    Close = db.Column(db.Integer, nullable=False)
    Volume = db.Column(db.Integer, nullable=False)
    wr14 = db.Column(db.Integer)

    def __repr__(self):
        return f'({self.__tablename__}: {self.Date}, {self.Open}, {self.Close})\n'


db.create_all()
quandl.ApiConfig.api_key = 'xQsG9W4sz9HzLpryaY5E'
df = quandl.get('EOD/HD', start_date='2000-12-28', end_date='2017-12-28')
df = df.reset_index()

for i in df.iloc[:].values:
    line = Stock(Date=i[0], Open=i[1], High=i[2], Low=i[3], Close=i[4], Volume=i[5])
    db.session.add(line)

# my_file = open('AMZN.csv')
# reader = csv.reader(my_file)

# for i in reader:
#     date = datetime.strptime(i[0], '%Y-%m-%d').date()
#     line = Stock(date=date, open=i[1], high=i[2], low=i[3], close=i[4], vol=i[5])
#     db.session.add(line)


db.session.commit()
print('uploaded')
