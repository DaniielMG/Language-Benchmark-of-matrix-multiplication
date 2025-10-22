
public class MatrixMultiplicationTest {

    public static void main(String[] args) {
        int[] matrixSizes = {256, 512, 1024, 2048};
        int runsPerSize = 5;

        for (int size : matrixSizes) {
            System.out.println("=== Matrix Size: " + size + "x" + size + " ===");
            double totalTime = 0.0;
            long totalMemory = 0;

            for (int run = 1; run <= runsPerSize; run++) {
                MatrixMultiplication mm = new MatrixMultiplication(size);
                mm.initializeMatrices();
                
                // --- Time and Memory Measurement ---
                long memoryBefore = getUsedMemory(); 
                long startTime = System.nanoTime();
                
                mm.multiply(); 
                
                long endTime = System.nanoTime();
                long memoryAfter = getUsedMemory();
                
                double elapsedTime = (endTime - startTime) / 1e9; 
                totalTime += elapsedTime;
                
                long memoryUsedBytes = (memoryAfter - memoryBefore); 
                double memoryUsedMB = memoryUsedBytes / (1024.0 * 1024.0);
                totalMemory += memoryUsedBytes;
                
                System.out.printf("Run %d: Time = %.3f seconds, Memory Used = %.2f MB%n",
                        run, elapsedTime, memoryUsedMB);
            }
            
            double averageTime = totalTime / runsPerSize;
            double averageMemoryMB = (totalMemory / runsPerSize) / (1024.0 * 1024.0);
            
            System.out.printf("Average: Time = %.3f seconds, Average Memory Used = %.2f MB%n%n",
                    averageTime, averageMemoryMB);
        }
    }

    private static long getUsedMemory() {
        Runtime runtime = Runtime.getRuntime();
        runtime.gc(); 
        return runtime.totalMemory() - runtime.freeMemory();
    }
}