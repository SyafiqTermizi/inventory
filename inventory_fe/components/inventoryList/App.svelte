<script lang="ts">
    import { onMount } from "svelte";

    let invetories: Inventory[] = [];

    onMount(async () => {
        fetch("/api/inventory")
            .then((response) => response.json())
            .then((data) => {
                invetories = data;
            })
            .catch((error) => {
                console.log(error);
                return [];
            });
    });
</script>

<table class="table">
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Supplier</th>
            <th scope="col">Availability</th>
        </tr>
    </thead>
    <tbody>
        {#each invetories as inventory}
            <tr>
                <th scope="row">{inventory.name}</th>
                <td>{inventory.supplier}</td>
                <td>{inventory.is_available}</td>
            </tr>
        {/each}
    </tbody>
</table>
