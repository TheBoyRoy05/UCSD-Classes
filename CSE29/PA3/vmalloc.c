#include "vm.h"
#include "vmlib.h"

/**
 * Finds the first best fit block in the heap for a given size.
 *
 * A best fit block is a free block that is the smallest block that
 * can fit the given size. If no such block exists, the function
 * returns NULL.
 *
 * @param size the size of the block to search for
 * @return the best fit block, or NULL if no such block exists
 */
struct block_header* find_best_fit(size_t size) {
    struct block_header* block = heapstart;
    struct block_header* best_fit = NULL;
    size_t min_size = SIZE_MAX;

    while (block->size_status != VM_ENDMARK) {
        if (!(block->size_status & VM_BUSY)) {
            if (BLKSZ(block) >= size && BLKSZ(block) < min_size) {
                min_size = BLKSZ(block);
                best_fit = block;
            }
        }
        block = (struct block_header*)(((char*)block) + BLKSZ(block));
    }
    return best_fit;
}

/**
 * Splits a free block into two smaller blocks: the first is used
 * and the second remains free.
 *
 * @param block the block to split
 * @param size the size of the used block
 */
void split_block(struct block_header* block, size_t size) {
    struct block_header* new_block = (struct block_header*)(((char*)block) + size);
    new_block->size_status = BLKSZ(block) - size;
    new_block->size_status |= VM_PREVBUSY;
    new_block->size_status &= ~VM_BUSY;

    char* footer_addr = ((char*)new_block) + BLKSZ(new_block) - sizeof(struct block_footer);
    struct block_footer* footer = (struct block_footer*)(footer_addr);
    footer->size = BLKSZ(new_block);
}

/**
 * Updates the size_status field of the given block and the 'previous block
 * status bit' of the next block.
 *
 * @param block the block to update
 * @param size the size of the allocated block
 */
void update_headers(struct block_header* block, size_t size) {
    block->size_status = size;
    block->size_status |= VM_BUSY;
    block->size_status |= VM_PREVBUSY;

    struct block_header* next_block = (struct block_header*)(((char*)block) + BLKSZ(block));
    if (next_block->size_status == VM_ENDMARK) return;
    next_block->size_status |= VM_PREVBUSY;
}

/**
 * Allocates a block of memory from the heap of the given size.
 *
 * @param size the size of the block to allocate
 * @return a pointer to the allocated block, or NULL if no such block exists
 */
void* vmalloc(size_t size) {
    if (size <= 0) return NULL;
    size = ROUND_UP(size + sizeof(struct block_header), BLKALIGN);

    struct block_header* block = find_best_fit(size);
    if (block == NULL) return NULL;

    if (BLKSZ(block) > size) split_block(block, size);
    update_headers(block, size);

    return (char*)block + sizeof(struct block_header);
}
