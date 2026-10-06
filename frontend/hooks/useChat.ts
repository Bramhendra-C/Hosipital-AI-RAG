"use client";

import { useState } from "react";
import api from "@/services/api";
import { Message, ChatResponse } from "@/types/chat";

export function useChat() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [loading, setLoading] = useState(false);

    async function askQuestion(question: string) {
        const response = await api.post<ChatResponse>("/chat", {
            question,
        });

        return response.data;
    }

    async function sendMessage(question: string) {
        if (!question.trim() || loading) {
            return;
        }

        const cleanQuestion = question.trim();

        const userMessage: Message = {
            role: "user",
            content: cleanQuestion,
        };

        setMessages((prev) => [...prev, userMessage]);
        setLoading(true);

        try {
            const data = await askQuestion(cleanQuestion);

            const assistantMessage: Message = {
                role: "assistant",
                content: data.answer,
                sources: data.sources,
            };

            setMessages((prev) => [...prev, assistantMessage]);

        } catch (error) {
            console.error("Chat request failed:", error);

            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    content:
                        "I'm unable to connect to the hospital AI service right now. Please try again in a moment.",
                    sources: [],
                },
            ]);

        } finally {
            setLoading(false);
        }
    }

    async function regenerateMessage(messageIndex: number) {
        if (loading || messageIndex <= 0) {
            return;
        }

        const previousMessage = messages[messageIndex - 1];

        if (previousMessage.role !== "user") {
            return;
        }

        setLoading(true);

        try {
            const data = await askQuestion(previousMessage.content);

            setMessages((prev) => {
                const updated = [...prev];

                updated[messageIndex] = {
                    role: "assistant",
                    content: data.answer,
                    sources: data.sources,
                };

                return updated;
            });

        } catch (error) {
            console.error("Regeneration failed:", error);

        } finally {
            setLoading(false);
        }
    }

    return {
        messages,
        loading,
        sendMessage,
        regenerateMessage,
    };
}