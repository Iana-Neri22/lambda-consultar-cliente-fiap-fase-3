import os
import sys
from typing import Dict, Any

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Lambda handler
def handler(event: Dict[str, Any], context: Any) -> Dict[str, bool]:
    return {'isAuthorized': False}