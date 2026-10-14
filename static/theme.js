(() => {
    const root = document.documentElement;
    const selector = document.getElementById("theme-select");
    const storageKey = "support-desk-theme";
    const validThemes = ["system", "light", "dark"];

    function getSavedTheme() {
        try {
            const saved = localStorage.getItem(storageKey);
            return validThemes.includes(saved) ? saved : "system";
        } catch {
            return "system";
        }
    }

    function applyTheme(theme) {
        if (theme === "system") {
            root.removeAttribute("data-theme");
        } else {
            root.setAttribute("data-theme", theme);
        }

        if (selector) {
            selector.value = theme;
        }

        const themeColor = document.querySelector(
            'meta[name="theme-color"]'
        );

        if (themeColor) {
            const dark = theme === "dark" ||
                (theme === "system" &&
                 window.matchMedia("(prefers-color-scheme: dark)").matches);

            themeColor.setAttribute(
                "content",
                dark ? "#151517" : "#f5f5f7"
            );
        }
    }

    let currentTheme = getSavedTheme();
    applyTheme(currentTheme);

    if (selector) {
        selector.addEventListener("change", () => {
            currentTheme = selector.value;
            applyTheme(currentTheme);

            try {
                localStorage.setItem(storageKey, currentTheme);
            } catch {
                // The theme still works if browser storage is unavailable.
            }
        });
    }

    const systemPreference = window.matchMedia(
        "(prefers-color-scheme: dark)"
    );

    systemPreference.addEventListener("change", () => {
        if (currentTheme === "system") {
            applyTheme("system");
        }
    });
})();
