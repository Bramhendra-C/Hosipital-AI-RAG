"use client";

import { Message } from "@/types/chat";
import ChatMessage from "./ChatMessage";
import WelcomeScreen from "./WelcomeScreen";
import LoadingMessage from "./LoadingMessage";
import { useAutoScroll } from "@/hooks/useAutoScroll";

interface ChatWindowProps {
    messages: Message[];
    loading: boolean;
    onSuggestion: (question: string) => void;
    onRegenerate: (messageIndex: number) => void;
}

export default function ChatWindow({
    messages,
    loading,
    onSuggestion,
    onRegenerate,
}: ChatWindowProps) {

    const bottomRef = useAutoScroll(
        `${messages.length}-${loading}`
    );

    if (messages.length === 0 && !loading) {
        return (
            <div className="flex-1 overflow-y-auto">
                <WelcomeScreen
                    onSuggestion={onSuggestion}
                />
            </div>
        );
    }

    return (
        <div className="flex-1 overflow-y-auto p-4 sm:p-6">
            <div className="mx-auto max-w-5xl">

                {messages.map((message, index) => (
                    <ChatMessage
                        key={index}
                        message={message}
                        messageIndex={index}
                        onRegenerate={onRegenerate}
                        loading={loading}
                    />
                ))}

                {loading && <LoadingMessage />}

                <div ref={bottomRef} />

            </div>
        </div>
    );
}