import os
import sys
import json

# Ensure project root is in path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

from sensi_workspace.agents.orchestrator import orchestrator

def test_earthquake_analysis():
    print("Testing Earthquake Analysis for Japan...")
    result = orchestrator.trigger_hazard_analysis("Tokyo, Japan", "Earthquake")
    print(f"Status: {result['status']}")
    assert result["success"] is True
    assert "logs" in result
    print("✅ Earthquake Analysis Test Passed")

def test_heatwave_analysis():
    print("\nTesting Heatwave Analysis for Europe...")
    result = orchestrator.trigger_hazard_analysis("Madrid, Spain", "Heatwave")
    print(f"Status: {result['status']}")
    assert result["success"] is True
    assert "logs" in result
    print("✅ Heatwave Analysis Test Passed")

if __name__ == "__main__":
    try:
        test_earthquake_analysis()
        test_heatwave_analysis()
        print("\nAll integration tests passed!")
    except Exception as e:
        print(f"\n❌ Test Failed: {e}")
        sys.exit(1)
