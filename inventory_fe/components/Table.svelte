<script lang="ts">
    export let inventories: Inventory[] = [];
    let basePillClass = "badge badge rounded-pill text-white px-2";
</script>

<table class="table table-hover">
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Supplier</th>
            <th scope="col">Availability</th>
        </tr>
    </thead>
    <tbody>
        {#each inventories as inventory}
            <tr>
                <td><a href={inventory.url}>{inventory.name}</a></td>
                <td>{inventory.supplier}</td>
                <td>
                    {#if inventory.is_available}
                        <span class="{basePillClass} bg-success">
                            Available
                        </span>
                    {:else}
                        <span class="{basePillClass} bg-danger">
                            Not available
                        </span>
                    {/if}
                </td>
            </tr>
        {/each}
    </tbody>
</table>
