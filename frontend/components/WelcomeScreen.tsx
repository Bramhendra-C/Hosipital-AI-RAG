"use client";

import {
    CalendarDays,
    CreditCard,
    Hospital,
    Phone,
    Search,
    Stethoscope,
} from "lucide-react";

interface WelcomeScreenProps {
    onSuggestion?: (question: string) => void;
}

const suggestions = [
    {
        label: "Smart Card",
        question: "What is a Smart Card?",
        icon: CreditCard,
    },
    {
        label: "Initial Deposit",
        question: "What is the initial deposit?",
        icon: Search,
    },
    {
        label: "Appointments",
        question: "How can I register for an appointment?",
        icon: CalendarDays,
    },
    {
        label: "Hospital Services",
        question: "What services are available at the hospital?",
        icon: Hospital,
    },
    {
        label: "Doctors & Departments",
        question: "What departments are available at the hospital?",
        icon: Stethoscope,
    },
    {
        label: "Contact",
        question: "What are the hospital contact details?",
        icon: Phone,
    },
];

export default function WelcomeScreen({
    onSuggestion,
}: WelcomeScreenProps) {

    return (
        <div className="flex flex-1 items-center justify-center overflow-y-auto px-4 py-10">

            <div className="w-full max-w-3xl text-center">

                {/* Main Icon */}
                <div className="mx-auto mb-6 flex h-20 w-20 items-center justify-center rounded-3xl bg-blue-50 shadow-sm">
                    <Hospital className="h-10 w-10 text-blue-600" />
                </div>

                {/* Heading */}
                <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
                    How can I help you?
                </h2>

                <p className="mx-auto mt-3 max-w-xl text-sm leading-6 text-gray-500 sm:text-base">
                    Ask questions about hospital services, registration,
                    appointments, charges, patient procedures and more.
                </p>

                {/* Suggested Questions */}
                <div className="mt-8">

                    <p className="mb-3 text-xs font-semibold uppercase tracking-wider text-gray-400">
                        Try asking
                    </p>

                    <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">

                        {suggestions.map((item) => {

                            const Icon = item.icon;

                            return (
                                <button
                                    key={item.label}
                                    type="button"
                                    onClick={() => onSuggestion?.(item.question)}
                                    className="group flex items-center gap-3 rounded-xl border border-gray-200 bg-white p-4 text-left shadow-sm transition-all hover:-translate-y-0.5 hover:border-blue-200 hover:shadow-md"
                                >

                                    <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-gray-50 transition-colors group-hover:bg-blue-50">
                                        <Icon className="h-4 w-4 text-gray-500 group-hover:text-blue-600" />
                                    </div>

                                    <div>
                                        <p className="text-sm font-semibold text-gray-800">
                                            {item.label}
                                        </p>

                                        <p className="mt-0.5 text-xs text-gray-500">
                                            {item.question}
                                        </p>
                                    </div>

                                </button>
                            );
                        })}

                    </div>
                </div>

                {/* Demo Watermark / Disclaimer */}
                <div className="mt-10">

                    <p className="text-[11px] font-medium uppercase tracking-[0.2em] text-gray-300">
                        Hospital AI Assistant
                    </p>

                    <p className="mx-auto mt-2 max-w-lg text-[11px] leading-5 text-gray-400">
                        Demo application built for document-grounded AI.
                        Information is generated from the provided hospital
                        documents and should not be considered medical advice
                        or an official hospital service.
                    </p>

                </div>

            </div>

        </div>
    );
}