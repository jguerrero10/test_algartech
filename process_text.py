import db
from models import InterfaceMap


def list_all():
    data = db.session.query(InterfaceMap).all()
    for i in data:
        print(i)


def main():
    with open('result.txt') as file:
        lines = file.readlines()

    for i in lines:
        if i.startswith('ip vrf'):
            ip_vrf = i[7:-3]
        if i.startswith(' route-target export'):
            route_target_export = i[22:-3]
            data = InterfaceMap(ip_vrf, route_target_export)
            db.session.add(data)
            db.session.commit()
            list_all()


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    main()


