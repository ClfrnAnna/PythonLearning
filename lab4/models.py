from sqlalchemy import MetaData
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, mapped_column

convention = {
    "all_column_names": lambda constraint, table: "_".join([column.name for column in constraint.columns.values()]),
    "ix": "ix__%(table_name)s__%(all_column_names)s",
    "uq": "uq__%(table_name)s__%(all_column_names)s",
    "ck": "ck__%(table_name)s__%(constraint_name)s",
    "fk": "fk__%(table_name)s__%(all_column_names)s__" "%(referred_table_name)s",
    "pk": "pk__%(table_name)s",
}

metadata_obj = MetaData(naming_convention=convention)


class Base(DeclarativeBase):
    metadata = metadata_obj


class QuestionModel(Base):
    __tablename__ = "questions"

    id = mapped_column(Integer, primary_key=True)
    question = mapped_column(String)
