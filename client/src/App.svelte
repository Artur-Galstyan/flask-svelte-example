<script>
    import { onMount } from "svelte";

    function logToConsole() {
        console.log("Hi");
    }

    onMount(() => {
        console.log("OnMount says hi!");
    });
</script>

Hi!

<button on:click={logToConsole}>Check your console :)</button>
