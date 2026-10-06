"use client";

import { Hospital, Circle } from "lucide-react";

export default function Header() {
    return (
        <header className="sticky top-0 z-20 border-b border-gray-200 bg-white/95 backdrop-blur">
            <div className="mx-auto flex h-16 max-w-6xl items-center justify-between px-4 sm:px-6">

                {/* Branding */}
                <div className="flex items-center gap-3">

                    <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-600 shadow-sm">
                        <Hospital className="h-6 w-6 text-white" />
                    </div>

                    <div>
                        <div className="flex items-center gap-2">
                            <h1 className="text-base font-bold text-gray-900 sm:text-lg">
                                Hospital AI Assistant
                            </h1>

                            <span className="rounded-full bg-blue-50 px-2 py-0.5 text-[10px] font-semibold uppercase tracking-wide text-blue-600">
                                Demo
                            </span>
                        </div>

                        <p className="hidden text-xs text-gray-500 sm:block">
                            Document-grounded hospital information assistant
                        </p>
                    </div>
                </div>

                {/* Status */}
                <div className="flex items-center gap-2 rounded-full border border-gray-200 bg-gray-50 px-3 py-1.5">

                    <Circle className="h-2.5 w-2.5 fill-emerald-500 text-emerald-500" />

                    <span className="text-xs font-medium text-gray-600">
                        AI Online
                    </span>

                </div>

            </div>
        </header>
    );
}