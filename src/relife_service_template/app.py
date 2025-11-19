from importlib.metadata import version

from fastapi import FastAPI

from relife_service_template.config.logging import configure_logging
from relife_service_template.routes import auth, examples, health

# Dynamically determine the package name
package_name = __name__.split(".")[0]

# Get version dynamically
package_dist_name = package_name.replace("_", "-")

try:
    __version__ = version(package_dist_name)
except ImportError:
    __version__ = "development"

configure_logging()

app = FastAPI(
    title="Technical Service APIs",
    description="FastAPI application for all technical indicators",
    version=__version__,
)

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(examples.router)

#Technical service endpoints
app.include_router(ee_router)
app.include_router(rei_router)
app.include_router(sei_router)
app.include_router(uc_router)
app.include_router(fv_router)