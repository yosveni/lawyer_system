from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from .routers import auth_router, schedule_router, task_router, matter_router, contact_router, activity_router, billing_router, request_router, payment_router, account_router
from ..domain.models.tenant import Base
from ..infrastructure.database import engine

app = FastAPI(
    title="Lawyer System API",
    description="API for managing legal services with multi-tenant support",
    version="1.0.0",
    openapi_tags=[
        {"name": "auth", "description": "User authentication and token generation"},
        # {"name": "tenants", "description": "Operations related to tenants"},
        {"name": "schedules", "description": "Manage schedules"},
        {"name": "tasks", "description": "Manage tasks"},
        {"name": "matters", "description": "Manage legal matters"},
        {"name": "contacts", "description": "Manage contacts"},
        {"name": "activities", "description": "Manage activities"},
        {"name": "billings", "description": "Manage billings"},
        {"name": "requests", "description": "Manage requests"},
        {"name": "payments", "description": "Manage payments"},
        {"name": "accounts", "description": "Manage accounts"}
    ]
)

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Configurar OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Incluir routers
app.include_router(auth_router.router, prefix="/auth", tags=["auth", "tenants"])
app.include_router(schedule_router.router, prefix="/api", tags=["schedules"])
app.include_router(task_router.router, prefix="/api", tags=["tasks"])
app.include_router(matter_router.router, prefix="/api", tags=["matters"])
app.include_router(contact_router.router, prefix="/api", tags=["contacts"])
app.include_router(activity_router.router, prefix="/api", tags=["activities"])
app.include_router(billing_router.router, prefix="/api", tags=["billings"])
app.include_router(request_router.router, prefix="/api", tags=["requests"])
app.include_router(payment_router.router, prefix="/api", tags=["payments"])
app.include_router(account_router.router, prefix="/api", tags=["accounts"])