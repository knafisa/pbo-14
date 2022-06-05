import time
import datetime
import abc

class Subject(object):
    def __init__(self):
        self.observers = []
        self.cur_time = None
    def register_observer(self,observer):
        if observer in self.observers:
            print (observer, 'sudah terregistrasi')
        else:
            self.observers.append(observer)
    def unregister_observer(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('observer tidak bisa di identifikasi')

    def notify_observer(self):
        self.cur_time=datetime.datetime.now()

        for observer in self.observers:
            observer.notify(self.cur_time)

class Observer(object, metaclass=abc.ABCMeta ):
    "abstract class untuk observer"
    @abc.abstractmethod
    def notify(self, unix_timestamp):
        pass

class NetworkObserver(Observer):
    "file log network "
    def __init__(self,name):
        self.name=name
    def notify(self, time):
        print(self.name, ':', time)


class SensorObserver(Observer):
    "file log network "

    def __init__(self, name):
        self.name = name

    def notify(self, time):
        print(self.name, ':', time)

class SecurityObserver(Observer):
    "file log network "

    def __init__(self, name):
        self.name = name

    def notify(self, time):
        print(self.name, ':', time)

if __name__=='__main__':
    subject = Subject()

    print('registrasi network observer')
    net_observer = NetworkObserver('network_observer')
    subject.register_observer(net_observer)
    subject.notify_observer()
    print()
    time.sleep(2)

    print('registrasi sensor observer')
    sensor_observer = SensorObserver('sensor_observer')
    subject.register_observer(sensor_observer)
    subject.notify_observer()
    print()
    time.sleep(2)

    print('unregistrasi network observer')
    subject.unregister_observer(net_observer)
    subject.notify_observer()
