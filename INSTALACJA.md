# Jak zainstalować skill

Każdy skill to jeden plik ZIP. Pobierz go z zakładki [Releases](../../releases/latest). Nie rozpakowuj go.

## Claude (claude.ai i aplikacja desktop)

Działa na każdym planie, także darmowym.

1. Otwórz claude.ai albo aplikację Claude na komputerze.
2. Sprawdź, czy masz włączone wykonywanie kodu: **Ustawienia → Capabilities → Code execution**.
3. Wejdź w **Customize → Skills**.
4. Kliknij **+**, potem **Create skill → Upload a skill**.
5. Wskaż pobrany plik ZIP.
6. Włącz skill przełącznikiem na liście.

Sprawdzenie: napisz w nowej rozmowie „Napisz reklamację wadliwego odkurzacza”. Claude powinien zacząć od pytań o dane do pisma.

## ChatGPT (chatgpt.com i aplikacja desktop)

Skille w ChatGPT są w wersji beta. Na koncie firmowym musi je włączyć administrator.

1. Otwórz chatgpt.com albo aplikację ChatGPT na komputerze.
2. W menu bocznym wybierz **Plugins**, potem zakładkę **Skills**.
3. Kliknij **Create → Upload from computer**.
4. Wskaż pobrany plik ZIP.
5. Kliknij **Install**.

Jeśli nie widzisz zakładki Skills, Twój plan albo workspace jeszcze jej nie ma.

## Gemini (gemini.google.com i aplikacja na Maca)

Działa na koncie osobistym Google, dla osób 18+. Wgrywanie plików działa w przeglądarce i w aplikacji na Maca.

1. Otwórz gemini.google.com.
2. Wejdź w **Ustawienia → Skills**.
3. Kliknij **Upload** i wskaż pobrany plik ZIP.

Gems znikają z kont osobistych w listopadzie 2026 i zamieniają się w skille. Ten skill trafi w to samo miejsce.

## Dla programistów

Ten sam folder ze `SKILL.md` działa bez zmian w Claude Code, Codex i Antigravity. Skopiuj folder skilla:

| Narzędzie | Folder |
|---|---|
| Claude Code | `~/.claude/skills/<nazwa>/` |
| Codex | `~/.agents/skills/<nazwa>/` |
| Antigravity | `~/.gemini/config/skills/<nazwa>/` |
