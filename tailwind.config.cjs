/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {},
		// fontFamily: {
		// 	sans: ['Libertine', 'sans-serif']
		// },
	},
	plugins: [require("@tailwindcss/typography"), require("daisyui")],
	daisyui: {
		themes: ["lofi", {
            "profile-dark": {
                "color-scheme": "dark",
                "base-100": "#191b20",
                "base-200": "#22252c",
                "base-300": "#363b45",
                "base-content": "#d3d6dc",
                "primary": "#d3d6dc",
                "primary-content": "#191b20",
                "secondary": "#95afff",
                "secondary-content": "#191b20",
                "accent": "#95afff",
                "accent-content": "#191b20",
                "neutral": "#363b45",
                "neutral-content": "#f1f2f5",
                "info": "#95afff",
                "success": "#89cda9",
                "warning": "#e6c27e",
                "error": "#ee9a9a",
                "--rounded-box": "1rem",
                "--rounded-btn": ".5rem",
                "--rounded-badge": "1.9rem",
            }
        }],
		darkTheme: "profile-dark", // name of one of the included themes for dark mode
		logs: false, // Shows info about daisyUI version and used config in the console when building your CSS
	}
}
