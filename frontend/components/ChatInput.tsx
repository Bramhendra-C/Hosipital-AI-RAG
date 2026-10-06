"use client";

import { useState } from "react";
import { Send } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

interface ChatInputProps {
    onSend: (question: string) => void;
    loading: boolean;
}

export default function ChatInput({
    onSend,
    loading,
}: ChatInputProps) {

    const [question, setQuestion] = useState("");

    function handleSend() {

        if (!question.trim() || loading) {
            return;
        }

        onSend(question.trim());
        setQuestion("");
    }

    return (
        <div className="border-t border-gray-200 bg-white/95 p-3 backdrop-blur sm:p-4">

            <div className="mx-auto max-w-5xl">

                <div className="flex items-center gap-2 rounded-2xl border border-gray-200 bg-gray-50 p-1.5 shadow-sm transition focus-within:border-blue-300 focus-within:ring-2 focus-within:ring-blue-100">

                    <Input
                        value={question}
                        placeholder={
                            loading
                                ? "Generating your answer..."
                                : "Ask anything about the hospital..."
                        }
                        disabled={loading}
                        className="border-0 bg-transparent shadow-none focus-visible:ring-0"
                        onChange={(e) => setQuestion(e.target.value)}
                        onKeyDown={(e) => {

                            if (
                                e.key === "Enter" &&
                                !e.shiftKey
                            ) {
                                e.preventDefault();
                                handleSend();
                            }

                        }}
                    />

                    <Button
                        onClick={handleSend}
                        disabled={loading || !question.trim()}
                        size="icon"
                        className="h-10 w-10 shrink-0 rounded-xl bg-blue-600 hover:bg-blue-700"
                    >

                        {loading ? (
                            <span className="h-4 w-4 animate-spin rounded-full border-2 border-white border-t-transparent" />
                        ) : (
                            <Send className="h-4 w-4" />
                        )}

                    </Button>

                </div>

                <p className="mt-2 text-center text-[10px] text-gray-400">
                    AI responses are based on the provided hospital documents.
                </p>

            </div>

        </div>
    );
}