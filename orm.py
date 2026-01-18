import os


from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ForeignKey, Enum, DateTime
from sqlalchemy.orm import declarative_base
from enum import Enum as PyEnum
from datetime import datetime








# Déclaration de la base qui servira à créer les modèles
Base = declarative_base()




class RoleType(PyEnum):
   CLIENT = "client"
   ADMIN = "admin"




# Définition des modèles
class Utilisateur(Base):
   __tablename__ = 'utilisateur'
 
   id = Column(Integer, primary_key=True)
   email = Column(String, nullable=False, unique=True)
   mot_de_passe = Column(String, nullable=False)
   nom = Column(String, nullable=False)
   role = Column(Enum(RoleType, name='role'), nullable=False)
   date_creation = Column(DateTime, default=datetime.now)


   def __repr__(self):
       return f"<Utilisateur(email='{self.email}', nom='{self.nom}'), role='{self.role}')>"




class Produit(Base):
   __tablename__ = 'produit'
  
   id = Column(Integer, primary_key=True)
   nom = Column(String, nullable=False)
   description = Column(Text)
   categorie = Column(String, nullable=False)
   prix = Column(Float, nullable=False)
   quantite_stock = Column(Integer, default=0)
   date_creation = Column(DateTime, default=datetime.now)


   def __repr__(self):
       return f"<Produit(nom='{self.nom}', description='{self.description}', categorie='{self.categorie}', prix='{self.prix}', quantite_stock='{self.quantite_stock}')>"



