from enum import Enum
import re


class QueryType(Enum):
    GENERIC = "generic"
    HOSPITAL = "hospital"
    OUT_OF_SCOPE = "out_of_scope"


GENERIC_PATTERNS = [
    r"^(hi|hello|hey|hai|hii)[!. ]*$",
    r"^(good morning|good afternoon|good evening)[!. ]*$",
    r"^(bye|goodbye|see you|see ya)[!. ]*$",
    r"^(thanks|thank you|thankyou)[!. ]*$",
    r"^(who are you)[?.! ]*$",
    r"^(what are you)[?.! ]*$",
    r"^(what can you do)[?.! ]*$",
    r"^(how can you help me)[?.! ]*$",
    r"^(what can you help me with)[?.! ]*$",
]


def classify_query(question: str) -> QueryType:

    question = question.strip().lower()

    # Empty input
    if not question:
        return QueryType.GENERIC

    # --------------------------------------------------
    # Generic conversational questions
    # --------------------------------------------------

    for pattern in GENERIC_PATTERNS:

        if re.fullmatch(pattern, question):
            return QueryType.GENERIC

    # --------------------------------------------------
    # Hospital-related keywords
    # --------------------------------------------------

    hospital_keywords = [
        "hospital",
        "doctor",
        "patient",
        "registration",
        "appointment",
        "opd",
        "emergency",
        "casualty",
        "smart card",
        "smartcard",
        "mri",
        "ct scan",
        "pet scan",
        "spect",
        "scan",
        "charges",
        "fee",
        "fees",
        "cost",
        "deposit",
        "refund",
        "billing",
        "payment",
        "blood bank",
        "transfusion",
        "pharmacy",
        "medicine",
        "teleconsultation",
        "report",
        "medical",
        "treatment",
        "cancer",
        "department",
        "service",
        "timing",
        "timings",
        "contact",
        "address",
    ]

    if any(keyword in question for keyword in hospital_keywords):
        return QueryType.HOSPITAL

    # --------------------------------------------------
    # Short conversational messages
    # --------------------------------------------------

    if len(question.split()) <= 3:

        conversational_words = [
            "okay",
            "ok",
            "thanks",
            "thank",
            "great",
            "nice",
            "cool",
            "awesome",
            "bye",
            "goodbye",
        ]

        if any(word in question.split() for word in conversational_words):
            return QueryType.GENERIC

    # --------------------------------------------------
    # Default
    # --------------------------------------------------

    return QueryType.OUT_OF_SCOPE