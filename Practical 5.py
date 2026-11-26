import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from practicals.practical_05_expert_system.logic import (
    analyze_loan,
    analyze_traffic,
    analyze_maintenance,
)


def main():
    print("=" * 64)
    print("  AI DECISION ARENA -- Rule-Based Expert Systems")
    print("=" * 64)

    loan = analyze_loan({
        "income": 65000,
        "credit_score": 760,
        "employment": "Permanent",
        "existing_loan": "No",
        "experience": 5,
        "loan_amount": 800000,
        "repayment_history": "Good",
    })
    print("\n[1] LOAN ELIGIBILITY ADVISOR")
    print(f"  Eligibility : {loan['eligibility']}")
    print(f"  Eligible %  : {loan['probability']['eligible']}%")
    print(f"  Factors     : {', '.join(loan['important_factors'])}")
    print(f"  Note        : {loan['ethics_note'][:70]}...")

    traffic = analyze_traffic({
        "lane_a": 45, "lane_b": 12, "lane_c": 8,
        "emergency": "Yes", "emergency_lane": "A",
    })
    print("\n[2] TRAFFIC SIGNAL DECISION")
    print(f"  Signals     : {traffic['signals']}")
    print(f"  Reason      : {traffic['reason']}")

    maint = analyze_maintenance({
        "temperature": 82,
        "vibration": "High",
        "pressure": "Normal",
        "cycle_time": 14,
        "production": "Below Target",
    })
    print("\n[3] MACHINE MAINTENANCE")
    print(f"  Status      : {maint['machine_status']}")
    print(f"  Risk        : {maint['risk_level']} ({maint['risk_score']})")
    print(f"  Area        : {maint['possible_area']}")
    print(f"  Action      : {maint['recommended_action']}")
    print("\nDone. Use the web UI for interactive Decision Arena forms.")


if __name__ == "__main__":
    main()
