import os
from dataclasses import asdict
from functools import lru_cache

from fastapi import APIRouter, HTTPException, status
from Communication.Responses.CustomerResponseJson import CustomerResponseJson
from Communication.Requests.CustomerRequestJson import CustomerRequestJson
from Communication.Enums.CustomerTypeJson import CustomerTypeJson

from Application.UseCases.Customer.CustomerInput import CustomerInput
from Application.UseCases.Customer.CreateCustomer.CreateCustomerUseCase import CreateCustomerUseCase
from Application.UseCases.Customer.GetCustomer.GetCustomersUseCase import GetCustomersUseCase

from Infrastructure.Database.SqliteDatabase import SqliteDatabase
from Infrastructure.Repositories.Customer.SqliteCustomerRepository import SqliteCustomerRepository


@lru_cache
def _get_customer_repository() -> SqliteCustomerRepository:
    db_path = os.getenv("APP_DB", "app.sqlite")
    database = SqliteDatabase(db_path)
    return SqliteCustomerRepository(database)

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("", response_model=CustomerResponseJson, status_code=status.HTTP_201_CREATED)
def create_customer(body: CustomerRequestJson):
    repository = _get_customer_repository()
    use_case = CreateCustomerUseCase(repository)
    try:
        customer_type = CustomerTypeJson.from_json(body.customer_type).value
        result = use_case.execute(
            CustomerInput(
                name=body.name,
                email=str(body.email),
                customer_type=customer_type,
                blocked=body.blocked,
            )
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    return CustomerResponseJson(**asdict(result))

@router.get("", response_model=list[CustomerResponseJson])
def get_customers():
    repository = _get_customer_repository()
    use_case = GetCustomersUseCase(repository)
    return [
        CustomerResponseJson(**asdict(customer))
        for customer in use_case.execute()
    ]
