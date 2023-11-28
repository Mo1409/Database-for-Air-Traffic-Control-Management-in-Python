from sqlalchemy import create_engine, select, desc
from utils.create_db import create_db
from sqlalchemy.orm import Session
from services.database import engine
from models.nationality import Nationality
from models.people import People
from models.route import Route
from models.company import Company
from models.plane import Plane
from models.employee import Employee
from models.trip import Trip
from models.passenger import Passenger
from models.maintenance import Maintenance
from models.contact import Contact
from models.passenger_has_trip import passenger_has_trip
from models.employee_has_trip import employee_has_trip
from models.people_has_nacionality import people_has_nacionality
from sqlalchemy import func

if __name__ == "__main__": 
    create_db()

engine = create_engine("mysql+pymysql://root:14092004@localhost:3306/controledetrafegofinal")

# Nacionalidades

with Session(engine) as session:

    Brasil = Nationality(
        country_name="Brasil", 
        continent="South America"
    )

    Espanha = Nationality(
        country_name="Espanha", 
        continent="Europa"
    )

    Alemanha = Nationality(
        country_name="Alemanha", 
        continent="Europa"
    )

    Italia = Nationality(
        country_name="Italia", 
        continent="Europa"
    )

    Argentina = Nationality(
        country_name="Argentina", 
        continent="South America"
    )

    Japao = Nationality(
        country_name="Japão", 
        continent="Ásia"
    )
    
session.add_all([Brasil, Espanha, Alemanha, Italia, Argentina, Japao])
session.commit()
    
#Pessoas

with Session(engine) as session:

    Gabriel = People(
        person_name = "Gabriel",
        cpf = "37834154036",
        rg = "343266532",
        birth_date = "2004-07-06"
    )

    Vini = People(
        person_name = "Vinicius",
        cpf = "72760264009",
        rg = "475135520",
        birth_date = "2005-09-13"
    )
    
    Mohamad = People(
        person_name = "Mohamad",
        cpf = "88467652063",
        rg = "321263005",
        birth_date = "2004-09-14"
    )

    Isabella = People(
        person_name = "Isabella",
        cpf = "46651713000",
        rg = "428699510",
        birth_date = "2004-09-17"
    )

    Vitor = People(
        person_name = "Vitor",
        cpf = "24125800065",
        rg = "369738597",
        birth_date = "2004-02-15"
    )

    Luca = People(
        person_name = "Luca",
        cpf = "21779161000",
        rg = "236346933",
        birth_date = "2004-05-26"
    )
    
    session.add_all([Gabriel, Vini, Mohamad, Isabella, Vitor, Luca])
    session.commit()

with Session(engine) as session:

# Rotas
 
    Br_Us = Route(
        country_departure='Brasil', 
        country_arrival='Estados Unidos', 
        expected_time='12', 
        city_departure='Manaus', 
        city_arrival='Nova York'
    )

    Us_Br = Route(
        country_departure='Estados Unidos', 
        country_arrival='Brasil', 
        expected_time='12', 
        city_departure='Nova York', 
        city_arrival='Curitiba'
    )

    Ar_Fr = Route(
        country_departure='Argentina', 
        country_arrival='França', 
        expected_time='13', 
        city_departure='Buenos Aires', 
        city_arrival='Paris'
    )

    Fr_Ar = Route(
        country_departure='França', 
        country_arrival='Argentina', 
        expected_time='13', 
        city_departure='Paris', 
        city_arrival='Buenos Aires'
    )

    Br_Ve = Route(
        country_departure='Brasil', 
        country_arrival='Venezuela', 
        expected_time='5', 
        city_departure='Manaus', 
        city_arrival='Caracas'
    )

    Uae_Isr = Route(
        country_departure='Emirados Árabes Unidos', 
        country_arrival='Israel', 
        expected_time='4', 
        city_departure='Jerusalem', 
        city_arrival='Dubai'
    )

    session.add_all([Br_Us, Us_Br, Ar_Fr, Fr_Ar, Br_Ve, Uae_Isr])
    session.commit()


# Companhias

with Session(engine) as session:

    Latam = Company(
        cnpj = "77.889.865/0001-85",
        company_name = 'LATAM'
    )

    Gol = Company(
        cnpj = "59.189.224/0001-36",
        company_name = 'GOL'
    )

    Emirates = Company(
        cnpj = "15.671.867/0001-46",
        company_name = 'EMIRATES'
    )

    Azul = Company(
        cnpj = "21.497.585/0001-77",
        company_name = 'AZUL'
    )

    Air_France = Company(
        cnpj = "19.030.199/0001-29",
        company_name = "AIR FRANCE"
    )

    Canada_Express = Company(
        cnpj = "12.277.205/0001-06",
        company_name = "CANADA EXPRESS"
    )

    session.add_all([Latam, Gol, Emirates, Azul, Air_France, Canada_Express])
    session.commit()

# Aviões

with Session(engine) as session:

    Airbus_A220 = Plane(
        model='Airbus A220',
        coord_x ='40.71145', 
        coord_y ='-74.01256', 
        coord_z ='1368', 
        company_id = '1'
    )
        
    Airbus_A380 = Plane(
        model = 'Airbus A380', 
        coord_x = '31.4421', 
        coord_y = '34.365053', 
        coord_z = '40000', 
        company_id = '2'
    )
    
    Boeing_707 = Plane(
        model ='Boeing 707', 
        coord_x ='39.44420', 
        coord_y ='125.733590', 
        coord_z ='27000', 
        company_id = '3'
    )
    
    Boeing_737 = Plane(
        model ='Boeing 737', 
        coord_x ='7.406752', 
        coord_y ='7.826526', 
        coord_z ='30000', 
        company_id = '4'
    )
    
    Antonov_An_225_Mriya = Plane(
        model ='Antonov An225 Mriya', 
        coord_x ='-25.431538', 
        coord_y ='-49.294847', 
        coord_z ='1000', 
        company_id = '5'
    )
    
    Douglas_DC_2 = Plane(
        model ='Douglas DC-2', 
        coord_x ='24.759363', 
        coord_y ='-77.958384', 
        coord_z ='20000', 
        company_id = '6'
    )
    
    session.add_all([Airbus_A220, Airbus_A380, Boeing_707, 
    Boeing_737, Antonov_An_225_Mriya, Douglas_DC_2])
    session.commit()

# Empregados

with Session(engine) as session:
        
    Employee1 = Employee(
        cnh ='34850788048',
        thefunction ='LIMPEZA', 
        people_id = '1'
    )
        
    Employee2 = Employee(
        cnh ='07452567224',
        thefunction ='PILOTO', 
        people_id ='2'
    )
        
    Employee3 = Employee(
        cnh ='53228423202',
        thefunction ='AEROBORDO', 
        people_id =  '3'
    )
        
    Employee4 = Employee(
        cnh ='29623731994', 
        thefunction ='PILOTO', 
        people_id ='4'
    )
        
    Employee5 = Employee(
        cnh ='55521432340',
        thefunction ='COPILOTO', 
        people_id ='5'
    )
        
    Employee6 = Employee(
        cnh ='16502167619',
        thefunction ='MANUTENCAO', 
        people_id = '6'
    )

    session.add_all([Employee1, Employee2, Employee3, Employee4, Employee5, Employee6])
    session.commit()

# Viagens

with Session(engine) as session:
        
    Trip1 = Trip(
        scheduled ='2023-05-25', 
        delay = 0,
        trip_status ='OK', 
        gate ='1', 
        route_id = '1', 
        plane_id = '1', 
        company_id = '1'
    )  
        
    Trip2 = Trip(
        scheduled ='2023-12-12', 
        delay = 0,
        trip_status ='OK', 
        gate ='2', 
        route_id = '2', 
        plane_id = '2', 
        company_id ='2'
    )
        
    Trip3 = Trip(
        scheduled ='2023-11-13', 
        delay = 0,
        trip_status ='OK', 
        gate ='3', 
        route_id = '3', 
        plane_id = '3', 
        company_id ='3'
    )
        
    Trip4 = Trip(
        scheduled ='2023-03-04', 
        delay = 0,
        trip_status ='OK', 
        gate ='4', 
        route_id = '4', 
        plane_id = '4', 
        company_id = '4'
    )
        
    Trip5 = Trip(
        scheduled ='2023-01-25',
        delay = 1,
        trip_status ='DELAY', 
        gate ='5', 
        route_id = '5', 
        plane_id = '5', 
        company_id = '5'
    )
        
    Trip6  = Trip(
        scheduled ='2023-11-09',
        delay = 1,
        trip_status ='DELAY', 
        gate ='6', 
        route_id = '6', 
        plane_id = '5', 
        company_id = '6'
    )
        
    session.add_all([Trip1, Trip2, Trip3, Trip4, Trip5, Trip6])
    session.commit()


# Passageiros

with Session(engine) as session:
    
    Passenger1 = Passenger(
        passport_num ='VQ718229', 
        visa = 1, 
        exp_date ='2028-02-17', 
        people_id = '1'
        )
    
    Passenger2 = Passenger(
        passport_num ='IR369175', 
        visa = 1, 
        exp_date ='2028-04-19', 
        people_id = '2'
        )
    
    Passenger3 = Passenger(
        passport_num ='LI371207', 
        visa = 1, 
        exp_date ='2028-01-31',
        people_id = '3'
        )
    
    Passenger4 = Passenger(
        passport_num ='TK658144', 
        visa = 1, 
        exp_date ='2028-05-21', 
        people_id = '4'
        )
    
    Passenger5 = Passenger(
        passport_num ='QU340528', 
        visa = 0, 
        exp_date ='2020-10-31', 
        people_id = '5'
        )
    
    Passenger6 = Passenger(
        passport_num ='X1TA0179', 
        visa = 0, 
        exp_date ='2021-09-13', 
        people_id = '6'
        )

    session.add_all([Passenger1, Passenger2, Passenger3, Passenger4, Passenger5, Passenger6])
    session.commit()

# Manutenção

with Session(engine) as session:

    Maintenance1 = Maintenance(
        plane_id = '1', 
        employee_id ='1', 
        maintenance_date ='2023-04-12'
    )
        
    Maintenance2 = Maintenance(
        plane_id = '2',
        employee_id ='2', 
        maintenance_date ='2023-05-11'
    )
        
    Maintenance3 = Maintenance(
        plane_id = '3',
        employee_id ='3', 
        maintenance_date ='2023-03-15'
    )
        
    Maintenance4 = Maintenance(
        plane_id = '5', 
        employee_id ='4', 
        maintenance_date ='2023-06-10'
    )
        
    Maintenance5 = Maintenance(
        plane_id = '5', 
        employee_id ='5', 
        maintenance_date ='2023-02-22'
    )
        
    Maintenance6 = Maintenance(
        plane_id = '6', 
        employee_id ='6', 
        maintenance_date ='2023-07-02'
    )
    
    session.add_all([Maintenance1, Maintenance2, Maintenance3, Maintenance4, Maintenance5, Maintenance6])
    session.commit()
        
#Contatos

with Session(engine) as session:
    
    Contato1 = Contact(
        id = '1', 
        people_id = '1', 
        phone ='4187781848', 
        email ='Gabriel.Schneider@pucpr.edu.br'
    )
    
    Contato2 = Contact(
        id = '2', 
        people_id = '2',  
        phone ='41995565859',
        email ='vini.yama13@gmail.com'
    )

    Contato3 = Contact(
        id = '3', 
        company_id = '3', 
        phone ='1149331205', 
        email ='latam@latam.com'
    )
    
    Contato4 = Contact(
        id = '4', 
        company_id = '4', 
        phone ='1149553144', 
        email ='gol@gol.com'
    )

    Contato5 = Contact(
        id = '5', 
        people_id = '5', 
        phone ='6999460287', 
        email ='isabellaberkembrock@pucpr.edu.br'
    )

    Contato6 = Contact(
        id = '6', 
        company_id = '6', 
        phone ='1154229908', 
        email ='flyemirates@emirates.com'
    )
    
    session.add_all([Contato1, Contato2, Contato3, Contato4, Contato5, Contato6])
    session.commit()
    
# Passageiros tem viagens

with Session(engine) as session:

    Passageiro_viagem1 = passenger_has_trip(
        trip_id = 1, 
        people_id = 1
    )
    
    Passageiro_viagem2 = passenger_has_trip(
        trip_id = 2, 
        people_id = 2
    )

    Passageiro_viagem3 = passenger_has_trip(
        trip_id = 3, 
        people_id = 3
    )

    Passageiro_viagem4 = passenger_has_trip(
        trip_id = 4, 
        people_id = 4
    )
    
    Passageiro_viagem5 = passenger_has_trip(
        trip_id = 5, 
        people_id = 4
    )

    Passageiro_viagem6 = passenger_has_trip(
        trip_id = 6, 
        people_id = 6
    )

    session.add_all([Passageiro_viagem1, Passageiro_viagem2, Passageiro_viagem3,
    Passageiro_viagem4, Passageiro_viagem5, Passageiro_viagem5, Passageiro_viagem6])
    session.commit()

#Empregados tem viagens

    Empregado_viagem1 = employee_has_trip(
    trip_id = 1, 
    people_id = 1
    )

    Empregado_viagem2 = employee_has_trip(
    trip_id = 2, 
    people_id = 4
    )
    
    Empregado_viagem3 = employee_has_trip(
    trip_id = 3, 
    people_id = 3
    )

    Empregado_viagem4 = employee_has_trip(
    trip_id = 4, 
    people_id = 4
    )

    Empregado_viagem5 = employee_has_trip(
    trip_id = 5, 
    people_id = 5
    )

    Empregado_viagem6 = employee_has_trip(
    trip_id = 6, 
    people_id = 6
    )

    session.add_all([Empregado_viagem1, Empregado_viagem2, Empregado_viagem3, 
    Empregado_viagem4, Empregado_viagem5, Empregado_viagem6])
    session.commit()

#Pessoas tem nacionalidades

with Session(engine) as session:

    Brasileiro = people_has_nacionality(
        people_id= 1, 
        nationality_id= 1
    )

    Espanhol = people_has_nacionality(
        people_id= 2, 
        nationality_id=2
    )
    
    Alemao = people_has_nacionality(
        people_id = 3, 
        nationality_id = 3
    )

    Italiano = people_has_nacionality(
        people_id = 4, 
        nationality_id = 4
    )

    Argentino = people_has_nacionality(
        people_id = 5, 
        nationality_id = 5
    )

    Japones = people_has_nacionality(
        people_id = 6, 
        nationality_id = 6
    )

    session.add_all([Brasileiro, Espanhol, Alemao, Italiano, Argentino, Japones])
    session.commit()

#Atualizando registros

stmt = select(Nationality).where(Nationality.country_name == "Espanha")
Espanha = session.scalars(stmt).one()

Espanha.country_name = "China"
Espanha.continent = "Asia"

session.commit()


stmt = select(Employee).where(Employee.people_id == 1)
Employee1 = session.scalars(stmt).one()

Employee1.thefunction = "MANUTENCAO"

session.commit()

stmt = select(Trip).where(Trip.id == 1)
Trip1 = session.scalars(stmt).one()

Trip1.delay = 1
Trip1.gate = 8

session.commit()

#Exclusao de registros

#session.delete(Airbus_A220)
#session.delete(Gabriel)
#session.delete(Brasil)
#session.delete(Italiano)
#session.delete(Trip1)

# Confirmar as exclusões?
#session.commit()


#Consultas

#1-País que mais recebeu passageiros

with Session(engine) as conn:
    most_received_country = conn.execute(
        select(Route.country_arrival, func.count().label("Quantidade que recebeu"))
        .join(Trip, Trip.route_id == Route.id)
        .join(passenger_has_trip, passenger_has_trip.trip_id == Trip.id)
        .join(Passenger, passenger_has_trip.people_id == Passenger.people_id)
        .group_by(Route.country_arrival)
        .order_by(desc("Quantidade que recebeu"))
    )
    print(f"País que mais recebeu passageiros: {most_received_country.first()}")

#2-País que mais exportou pessoas

with Session(engine) as conn:
    most_exported_country = conn.execute(
        select(Route.country_departure, func.count().label("Quantidade que exportou"))
        .join(Trip, Trip.route_id == Route.id)
        .join(passenger_has_trip, passenger_has_trip.trip_id == Trip.id)
        .join(Passenger, passenger_has_trip.people_id == Passenger.people_id)
        .group_by(Route.country_departure)
        .order_by(desc("Quantidade que exportou"))
    )
    print(f"País que mais exportou pessoas: {most_exported_country.first()}")

#3-Cidade brasileira que mais recebeu passageiros

with Session(engine) as conn:
    most_received_brazilian_city = conn.execute(
        select(Route.city_arrival, func.count().label("Quantidade que recebeu"))
        .join(Trip, Trip.route_id == Route.id)
        .join(passenger_has_trip, passenger_has_trip.trip_id == Trip.id)
        .join(Passenger, passenger_has_trip.people_id == Passenger.people_id)
        .filter(Route.country_arrival == 'Brasil')
        .group_by(Route.city_arrival)
        .order_by(desc("Quantidade que recebeu"))
    )
    print(f"Cidade brasileira que mais recebeu passageiros: {most_received_brazilian_city.first()}")

#4-Cidades brasileiras que mais exportaram passageiros

with Session(engine) as conn:
    most_exported_brazilian_city = conn.execute(
        select(Route.city_departure, func.count().label("Quantidade que exportou"))
        .join(Trip, Trip.route_id == Route.id)
        .join(passenger_has_trip, passenger_has_trip.trip_id == Trip.id)
        .join(Passenger, passenger_has_trip.people_id == Passenger.people_id)
        .filter(Route.country_departure == 'Brasil')
        .group_by(Route.city_departure)
        .order_by(desc("Quantidade que exportou"))
    )
    print(f"Cidade brasileira que mais exportou passageiros: {most_exported_brazilian_city.first()}")

#5-Capitais mais visitadas

with Session(engine) as conn:
    most_visited_capitals = conn.execute(
        select(Route.city_arrival, func.count().label("Quantidade que recebeu")).where(Route.city_arrival.in_(["Curitiba", "Paris","Buenos Aires", "Caracas"]))
        .join(Trip, Trip.route_id == Route.id)
        .join(passenger_has_trip, passenger_has_trip.trip_id == Trip.id)
        .join(Passenger, passenger_has_trip.people_id == Passenger.people_id)
        .group_by(Route.city_arrival)
        .order_by(desc("Quantidade que recebeu"))
    )
    print(f"Capitais mais visitadas: {most_visited_capitals.all()}")

#6-Cidades extrangeiras que mais exportaram passageiros

with Session(engine) as conn:
    most_exported_foreign_city = conn.execute(
        select(Route.city_departure, func.count().label("Quantidade que exportou"))
        .join(Trip, Trip.route_id == Route.id)
        .join(passenger_has_trip, passenger_has_trip.trip_id == Trip.id)
        .join(Passenger, passenger_has_trip.people_id == Passenger.people_id)
        .filter(Route.country_departure != 'Brasil')
        .group_by(Route.city_departure)
        .order_by(desc("Quantidade que exportou"))
    )
    print(f"Cidades extrangeiras que mais exportou passageiros: {most_exported_foreign_city.all()}")


#7-Continente de quem mais viajou
with Session(engine) as conn:
    most_traveled_continent = conn.execute(
        select(Nationality.continent, func.count().label('Quantidade de viagens')) 
        .join(people_has_nacionality, Nationality.id == people_has_nacionality.nationality_id) 
        .join(passenger_has_trip, people_has_nacionality.people_id == passenger_has_trip.people_id) 
        .join(Trip, passenger_has_trip.trip_id == Trip.id) 
        .group_by(Nationality.continent) 
        .order_by(desc(func.count()))
    )
    print(f"Continente de quem mais viajou: {most_traveled_continent.all()}")

#8-Pessoas que mais viajaram

with Session(engine) as conn:
    most_traveled_person = conn.execute(
        select(People.id, People.person_name, func.count().label("Quantidade de viagens"))
        .join(Passenger, People.id == Passenger.people_id)
        .join(passenger_has_trip, passenger_has_trip.people_id == Passenger.people_id) 
        .group_by(Passenger.people_id)
        .order_by(desc("Quantidade de viagens"))
        )
    print(f"Pessoas que mais viajaram: {most_traveled_person.all()}")

#9-Nacionalidades que mais viajaram

with Session(engine) as conn:
    most_traveled_nationality = conn.execute(
        select(Nationality.country_name, func.count().label('Quantidade de viagens')) 
        .join(people_has_nacionality, Nationality.id == people_has_nacionality.nationality_id) 
        .join(passenger_has_trip, people_has_nacionality.people_id == passenger_has_trip.people_id) 
        .join(Trip, passenger_has_trip.trip_id == Trip.id) 
        .group_by(Nationality.country_name) 
        .order_by(desc(func.count()))
    )
    print(f"Nacionalidades que mais viajaram: {most_traveled_nationality.all()}")

#10-Nacionalidades que menos viajaram

with Session(engine) as conn:
    most_traveled_nationality = conn.execute(
        select(Nationality.country_name, func.count().label('Quantidade de viagens')) 
        .join(people_has_nacionality, Nationality.id == people_has_nacionality.nationality_id) 
        .join(passenger_has_trip, people_has_nacionality.people_id == passenger_has_trip.people_id) 
        .join(Trip, passenger_has_trip.trip_id == Trip.id) 
        .group_by(Nationality.country_name) 
        .order_by((func.count().asc()))
    )
    print(f"Nacionalidades que menos viajaram: {most_traveled_nationality.all()}")

#11-Aviões que mais viajaram

with Session(engine) as conn:
    most_traveled_nationality = conn.execute(
        select(Plane.model, func.count().label('Quantidade de viagens'))
        .join(Trip, Trip.plane_id == Plane.id)
        .group_by(Plane.id) 
        .order_by(func.count(Trip.id).desc())
        )
    print(f"Aviões que mais viajaram: {most_traveled_nationality.all()}")

#12-Quantidade de aviões

with Session(engine) as conn:
    total_planes = conn.execute(
        select(func.count(Plane.id).label("Total de aviões"))
    ).scalar()

    print(f"Total de aviões: {total_planes}")


#13-Aviões que menos viajaram

with Session(engine) as conn:
    least_traveled_planes = conn.execute(
        select(Plane.model, func.count(Trip.id).label('Quantidade de viagens'))
        .join(Trip, Trip.plane_id == Plane.id)
        .group_by(Plane.id) 
        .order_by(func.count(Trip.id).asc())
        )
    print(f"Avião que menos viajou: {least_traveled_planes.all()}")

#14-Avioes que menos estiveram em manutenção 

with Session(engine) as conn:
    least_maintained_planes = conn.execute(
        
        select(Plane.id,Plane.model,func.count(Maintenance.plane_id).label('Quantidade de manutenções'))
        .outerjoin(Maintenance,Plane.id == Maintenance.plane_id)
        .group_by(Plane.id)
        .order_by(func.count(Maintenance.plane_id).asc())
        )
    print(f"Avião que menos teve menos manutenções: {least_maintained_planes.all()}")


#15-Tempo de cada viagem

with Session(engine) as conn:
    trip_durations = conn.execute(
        select( Trip.id, Route.expected_time)
        .join(Route, Route.id == Trip.id)
        .group_by(Route.expected_time, Trip.id)
        .order_by(func.count(Trip.id))
    )
    print(f"Tempo de cada viagem: {trip_durations.all()}")


#16-Empregados que mais viajaram

with Session(engine) as conn:
    most_traveled_employees = conn.execute(
        select(People.id, People.person_name, func.count().label("Quantidade de viagens"))
        .join(Employee, People.id == Employee.people_id)
        .join(employee_has_trip, employee_has_trip.people_id == Employee.people_id) 
        .group_by(Employee.people_id)
        .order_by(desc("Quantidade de viagens"))
        )
    print(f"Empregado que mais viajou: {most_traveled_employees.first()}")


#17-Pilotos que tiveram mais horas de voo

with Session(engine) as conn:
    most_hour_pilots = conn.execute(
        select(
            Employee.people_id,
            People.person_name,
            func.sum(Route.expected_time).label("Quantidade de Horas Viajadas")
        )
        .join(People, People.id == Employee.people_id)
        .join(employee_has_trip, Employee.people_id == employee_has_trip.people_id)
        .join(Trip, Trip.id == employee_has_trip.trip_id)
        .join(Route, Trip.route_id == Route.id)
        .filter(Employee.thefunction == 'PILOTO')
        .group_by(Employee.people_id)
        .order_by(func.sum(Route.expected_time).desc())  
    )
    print(f"Pilotos que tiveram mais horas de voo: {most_hour_pilots.all()}")

#18-Total de pessoas que viajaram

with Session(engine) as conn:
    total_people_traveled = conn.execute(
        select(func.count().label("Total de pessoas"))
        .select_from(People)
        .join(passenger_has_trip, People.id == passenger_has_trip.people_id)
    ).scalar()

    print(f"Total de pessoas que viajaram: {total_people_traveled}")

#19-Total de viagens 

with Session(engine) as conn:
    total_trips = conn.execute(
    select(func.count(Trip.id).label("Total de viagens"))
    ).scalar()

    print(f"Total de viagens: {total_trips}")


#20-Companhia que mais fez viajens

with Session(engine) as conn:
    most_active_company = conn.execute(
        select(Company.company_name , func.count(Trip.id).label('Quantidade de viagens'))
        .join(Trip, Trip.company_id == Company.id)
        .group_by(Company.company_name) 
        .order_by(func.count(Trip.id).desc())
        )
    print(f"Companhia que mais realizou viagens: {most_active_company.first()}")
