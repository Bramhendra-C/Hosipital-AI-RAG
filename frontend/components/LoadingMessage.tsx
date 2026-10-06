"use client";

import { useEffect, useState } from "react";

const loadingMessages = [
    "Searching hospital documents",
    "Analyzing relevant information",
    "Generating your answer",
];

export default function LoadingMessage() {
    const [step, setStep] = useState(0);

    useEffect(() => {
        const interval = setInterval(() => {
            setStep((current) => (current + 1) % loadingMessages.length);
        }, 1400);

        return () => {
            clearInterval(interval);
        };
    }, []);

    return (
        <div className="flex justify-start px-4 py-3">
            <div className="flex max-w-[75%] items-center gap-3 rounded-2xl rounded-bl-md border border-gray-200 bg-white px-5 py-4 shadow-sm">

                {/* AI Icon */}
                <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-blue-600 text-white">
                    🤖
                </div>

                {/* Loading Content */}
                <div>
                    <div className="text-sm font-medium text-gray-700">
                        {loadingMessages[step]}
                    </div>

                    {/* Animated dots */}
                    <div className="mt-2 flex items-center gap-1">
                        <span className="h-1.5 w-1.5 animate-bounce rounded-full bg-blue-500 [animation-delay:-0.3s]" />

                        <span className="h-1.5 w-1.5 animate-bounce rounded-full bg-blue-500 [animation-delay:-0.15s]" />

                        <span className="h-1.5 w-1.5 animate-bounce rounded-full bg-blue-500" />
                    </div>
                </div>

            </div>
        </div>
    );
}