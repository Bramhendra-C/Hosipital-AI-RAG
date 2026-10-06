"use client";

import { useState } from "react";
import ReactMarkdown from "react-markdown";
import { Copy, Check, RefreshCw } from "lucide-react";

import { Message } from "@/types/chat";

interface ChatMessageProps {
    message: Message;
    messageIndex: number;
    onRegenerate: (messageIndex: number) => void;
    loading: boolean;
}

export default function ChatMessage({
    message,
    messageIndex,
    onRegenerate,
    loading,
}: ChatMessageProps) {

    const isUser = message.role === "user";

    const [copied, setCopied] = useState(false);

    async function handleCopy() {
        try {
            await navigator.clipboard.writeText(message.content);

            setCopied(true);

            setTimeout(() => {
                setCopied(false);
            }, 1500);

        } catch (error) {
            console.error("Copy failed:", error);
        }
    }

    return (
        <div
            className={`mb-6 flex ${isUser ? "justify-end" : "justify-start"
                }`}
        >

            <div
                className={`max-w-3xl rounded-2xl p-5 shadow-sm ${isUser
                    ? "bg-blue-600 text-white"
                    : "border border-gray-200 bg-white text-gray-900"
                    }`}
            >

                {/* Message */}

                {isUser ? (
                    <p className="whitespace-pre-wrap leading-relaxed">
                        {message.content}
                    </p>
                ) : (
                    <div className="prose prose-sm max-w-none text-gray-900">

                        <ReactMarkdown
                            components={{
                                p: ({ children }) => (
                                    <p className="mb-3 leading-7 last:mb-0">
                                        {children}
                                    </p>
                                ),

                                strong: ({ children }) => (
                                    <strong className="font-semibold text-gray-900">
                                        {children}
                                    </strong>
                                ),

                                ul: ({ children }) => (
                                    <ul className="mb-4 ml-5 list-disc space-y-1.5">
                                        {children}
                                    </ul>
                                ),

                                ol: ({ children }) => (
                                    <ol className="mb-4 ml-5 list-decimal space-y-1.5">
                                        {children}
                                    </ol>
                                ),

                                h1: ({ children }) => (
                                    <h1 className="mb-3 mt-4 text-xl font-bold">
                                        {children}
                                    </h1>
                                ),

                                h2: ({ children }) => (
                                    <h2 className="mb-3 mt-4 text-lg font-bold">
                                        {children}
                                    </h2>
                                ),

                                h3: ({ children }) => (
                                    <h3 className="mb-2 mt-4 text-base font-semibold">
                                        {children}
                                    </h3>
                                ),

                                hr: () => (
                                    <hr className="my-4 border-gray-200" />
                                ),
                            }}
                        >
                            {message.content}
                        </ReactMarkdown>

                    </div>
                )}

                {/* Assistant Actions */}

                {!isUser && (
                    <div className="mt-4 flex items-center gap-2 border-t border-gray-100 pt-3">

                        <button
                            type="button"
                            onClick={handleCopy}
                            className="flex items-center gap-1.5 rounded-lg px-2.5 py-1.5 text-xs font-medium text-gray-500 transition hover:bg-gray-100 hover:text-gray-800"
                        >
                            {copied ? (
                                <>
                                    <Check className="h-3.5 w-3.5 text-green-600" />
                                    Copied
                                </>
                            ) : (
                                <>
                                    <Copy className="h-3.5 w-3.5" />
                                    Copy
                                </>
                            )}
                        </button>

                        <button
                            type="button"
                            disabled={loading}
                            onClick={() => onRegenerate(messageIndex)}
                            className="flex items-center gap-1.5 rounded-lg px-2.5 py-1.5 text-xs font-medium text-gray-500 transition hover:bg-gray-100 hover:text-gray-800 disabled:cursor-not-allowed disabled:opacity-40"
                        >
                            <RefreshCw
                                className={`h-3.5 w-3.5 ${loading ? "animate-spin" : ""
                                    }`}
                            />

                            Regenerate
                        </button>

                    </div>
                )}

                {/* Sources */}

                {!isUser &&
                    message.sources &&
                    message.sources.length > 0 && (

                        <div className="mt-5 border-t border-gray-100 pt-4">

                            <h3 className="mb-3 text-sm font-semibold text-gray-700">
                                Sources
                            </h3>

                            <div className="space-y-2">

                                {message.sources.map((source, index) => (

                                    <div
                                        key={`${source.source}-${source.page}-${index}`}
                                        className="rounded-xl border border-gray-200 bg-gray-50 p-3 transition hover:bg-gray-100"
                                    >

                                        <div className="flex items-start gap-2">

                                            <span className="text-base">
                                                📄
                                            </span>

                                            <div>

                                                <p className="text-sm font-medium text-gray-800">
                                                    {source.source}
                                                </p>

                                                <p className="mt-1 text-xs text-gray-500">
                                                    Page {source.page}
                                                </p>

                                            </div>

                                        </div>

                                    </div>

                                ))}

                            </div>

                        </div>
                    )}

            </div>
        </div>
    );
}