import psycopg2


def main():
    conn = psycopg2.connect(
        "postgresql://testveloree_user:Hrc2UR6KHgvp2SbN2YUQt10TAY3vqHWq@dpg-cumudbij1k6c73b42spg-a.oregon-postgres.render.com/testveloree")
    conn.close()


if __name__ == '__main__':
    main()
