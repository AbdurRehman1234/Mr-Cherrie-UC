
import sys
from datetime import datetime
from scrapy.http import Request
from scrapy.exceptions import DropItem
import hashlib
import MySQLdb
from itemadapter import ItemAdapter


created_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class FareastScraperPipeline:
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', '',
                                    'fareastholdingsb_yahoo', charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def check_data_existance(self, item):
        mydata_queue = []

        try:
            self.cursor.execute("""SELECT * FROM yahoo WHERE high= %(high)s and low= %(low)s and volume= %(volume)s
            and volume_bs= %(volume_bs)s and price_bid_per_ask=%(price_bid_per_ask)s and 52w=%(52w)s and roe=%(roe)s and
        p_b=%(p_b)s and eps=%(eps)s and dps=%(dps)s and dy=%(dy)s and nta=%(nta)s and p_e=%(p_e)s""", {
            'high': item['High'], 'low': item['Low'], 'volume': item['Volume'], 'volume_bs': item['volume_bs'],
            'price_bid_per_ask': item['price'], '52w': item['fiftytwoW'], 'roe': item['ROE'], 'p_b': item['PB'],
        'eps': item['EPS'], 'dps': item['DPS'], 'dy': item['DY'], 'nta': item['NTA'], 'p_e': item['PE']

        })
            myresults = self.cursor.fetchone()
            for x in myresults:
                # for x in row:
                mydata_queue.append(x)
            print(f"my data queue is {mydata_queue}")
        except:
            print('error occured')

        if (item['High'] and item['Low'] and item['Volume'] and item['volume_bs'] and item['price'] and
                                item['fiftytwoW'] and item['ROE'] and item['PB'] and item['EPS'] and item['DPS'] and
                                item['DY'] and item['NTA'] and item['PE']) in mydata_queue:
            return False
        else:
            return True

    def process_item(self, item, spider):
        try:
            check = self.check_data_existance(item)
            if(check==False):
                print("dont insert data")
            else:
                self.cursor.execute("""INSERT INTO yahoo (high, low, volume, volume_bs, price_bid_per_ask, 52w, roe, p_b, eps, dps, dy,
                nta, p_e, rps, psr, market_cap, Shares_mil, rsi_14, stochastic_14, average_vol_3mil, last_done, percentage_chg, change_p, created_datetime)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                                    (item['High'], item['Low'], item['Volume'], item['volume_bs'], item['price'],
                                    item['fiftytwoW'], item['ROE'], item['PB'], item['EPS'], item['DPS'],
                                    item['DY'], item['NTA'], item['PE'], item['RPS'], item['PSR'],
                                    item['Market_cap'], item['Shares'], item['RSI'], item['Stochastic14'], item['Average3M'],
                                    item['last_done'], item['percent_change'], item['change'], created_datetime))
            # self.conn.commit()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
        return item
