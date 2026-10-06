import { Hospital } from "lucide-react";

export default function Footer() {
    return (
        <footer className="border-t border-gray-200 bg-white px-4 py-3">
            <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-2 text-center sm:flex-row sm:text-left">

                <div>
                    <p className="text-xs font-medium text-gray-600">
                        Hospital AI Assistant
                    </p>

                    <p className="text-[10px] text-gray-400">
                        RAG • FAISS • Cross-Encoder • Gemini • FastAPI • Next.js
                    </p>
                </div>

                <div className="flex items-center gap-3">

                    <p className="text-[10px] text-gray-400">
                        Portfolio Demo • 2026
                    </p>

                    <a
                        href="https://github.com/"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="rounded-lg px-2 py-1 text-xs font-medium text-gray-500 transition hover:bg-gray-100 hover:text-gray-800"
                    >
                        GitHub
                    </a>

                </div>

            </div>
        </footer>
    );
}