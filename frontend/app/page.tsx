"use client";

import Header from "@/components/Header";
import ChatWindow from "@/components/ChatWindow";
import ChatInput from "@/components/ChatInput";
import Footer from "@/components/Footer";

import { useChat } from "@/hooks/useChat";

export default function Home() {
  const {
    messages,
    loading,
    sendMessage,
    regenerateMessage,
  } = useChat();

  return (
    <main className="flex h-screen flex-col bg-gray-50">

      <Header />

      <ChatWindow
        messages={messages}
        loading={loading}
        onSuggestion={sendMessage}
        onRegenerate={regenerateMessage}
      />

      <ChatInput
        onSend={sendMessage}
        loading={loading}
      />

      <Footer />

    </main>
  );
}