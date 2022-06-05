class Weather_station:
    
    value_sensor="00.0"
    monitoring="pie chart"
    timestamp="8/06/2021"
    status_sensor="on"

    def __init__(self, status_sensor ):
        self.status_sensor = status_sensor
        print('weather station ready')
    def value_sensor(self):
        return "00.00"
        
        
    def timestamp(self, timestamp):
        self.timestamp=timestamp
        print('waktu pengukuran'+self.timestamp)
        
    def change_monitoring(self, chart='diagram batang'):
        self.monitoring=chart
        print('tampilan monitoring '+ self.monitoring)
        
    def get_monitoring(self):
        return self.monitoring
    def get_sensor(value):
        print(value.value_sensor())
        
        
        
class Sensor_suhu(Weather_station):
    def value_sensor(self):
        return '24.0'
    
   

weather = Weather_station('on')
weather.change_monitoring(' chart batang')
weather.timestamp('10/06/2021')
weather_suhu=Weather_station('on')
monitoring = weather_suhu.get_monitoring()
print(monitoring)